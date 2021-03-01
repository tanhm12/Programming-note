import torch
import os
import time
import pickle
import numpy as np

from torch import nn
from tqdm import tqdm
from sklearn.metrics import classification_report

model = nn.Sequential(nn.Linear(10, 10))  # sample model
optimizer = torch.optim.Adam(model.parameters())  # sample optimizer
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.9)  # sample scheduler

device = 'cuda'
SAVE_DIR = '/content/drive/MyDrive/Tan/checking/extractive-document-summarization/save/cnn-dailymail-new'

if not os.path.exists(SAVE_DIR):
    os.mkdir(SAVE_DIR)

# model.load_state_dict(torch.load(os.path.join(SAVE_DIR, 'model_2.pt')))
# model.to(device)


def train(x, y, epochs, batch_size, print_freq=0.1,
          save_dir=SAVE_DIR):
    best_dev_loss = 1e9
    model.train()
    i = 0
    print_after = int(print_freq * len(x) / batch_size)
    start_time = time.time()
    all_train_loss = []
    all_dev_loss = []
    for epoch in range(epochs):
        print_counter = 0
        total_loss = []
        print('epoch:', epoch)
        for i in tqdm(range(0, len(x), batch_size)):
            prob, loss = model.forward(x[i: i + batch_size],
                                       y[i: i + batch_size],
                                       )
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1)
            optimizer.step()
            total_loss.append(loss.item())
            if i > print_counter:
                print('step: {}, loss: {}, total loss: {}'.format(i, loss.item(), np.mean(total_loss)))
                print_counter += print_after
        scheduler.step()
        model.save(os.path.join(save_dir, 'model_{}.pt'.format(str(epoch))))
        print('train loss:', np.mean(total_loss))
        dev_loss = eval()
        print('dev_loss:', dev_loss)
        if dev_loss < best_dev_loss:
            model.save(os.path.join(save_dir, 'best-model.pt'))
            best_dev_loss = dev_loss
        # all_train_loss.append(total_loss)
        # all_dev_loss.append(dev_loss)
        end_time = time.time()
        print('Finish epoch {} at {}, in {} seconds. \n'.format(epoch, end_time, end_time - start_time))
        with open(os.path.join(save_dir, 'train_loss_{}.pkl'.format(epoch)), 'wb') as f:
            pickle.dump(total_loss, f, protocol=pickle.HIGHEST_PROTOCOL)
        with open(os.path.join(save_dir, 'dev_loss_{}.pkl'.format(epoch)), 'wb') as f:
            pickle.dump(dev_loss, f, protocol=pickle.HIGHEST_PROTOCOL)


def eval(x, y, batch_size, get_report=True):
    model.eval()
    total_loss = []
    y_pred = []
    y_true = []

    for i in y:
        y_true.extend(i.tolist())

    with torch.no_grad():
        for i in range(0, len(x), batch_size):
            prob, loss = model.forward(x[i: i + batch_size],
                                       y[i: i + batch_size],
                                       )

            temp_y_pred = [0 for _ in range(len(y[i: i + batch_size]))]
            for j, sent in enumerate(y[i: i + batch_size]):
                temp_prob = np.argsort(prob[j][:len(sent)].tolist())
                temp_y_pred[j] = [0] * len(sent)
                # print(temp_prob)
                for k in temp_prob[-4:]:
                    temp_y_pred[j][k] = 1
            for sent in temp_y_pred:
                y_pred.extend(sent)
            total_loss.append(loss.item())

    if get_report:
        print(classification_report(y_true, y_pred))

    model.train()

    return np.mean(total_loss)