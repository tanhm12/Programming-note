# OSI model
- <MAC><IP><TCP/IP><HTTP>
- MAC address chỉ dùng để trỏ đến vị trí hiện tại và next hop, thay đổi khi tới hop
- Tìm địa chỉ router thông qua IP
- Tìm địa chỉ service/app thông qua port (tcp/udp), trong trường hơp mạng local (nhiều PCs) thì router map port của máy sang port của router (trường hơp gateway thì tương tự: gateway là router, router sẽ là PC). Vì vậy 1 router chỉ có 1 ip address, http trỏ tới cổng 80 trên router.