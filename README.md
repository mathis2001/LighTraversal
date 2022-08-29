# LighTraversal
LighTraversal is a tool designed to find basic path traversal vulnerabities

## Install:
```bash
$ git clone https://github.com/mathis2001/LighTraversal
```

## Usage:
```bash
$ cat urls.txt | python3 LighTraversal.py [--null-byte]

or with an other tool like ParamFirstCheck

$ cat urls.txt | python3 ParamFirstCheck.py --lfi | python3 LighTraversal.py [--null-byte]
```

## Screenshots:

![image](https://user-images.githubusercontent.com/40497633/186877980-f9066c3b-7b4f-4de9-b67e-7cca75f1fc3f.png)
![image](https://user-images.githubusercontent.com/40497633/186878157-04f5816a-cb17-42e0-8ce3-c217ea3eb1ab.png)
![image](https://user-images.githubusercontent.com/40497633/186878549-c0963b13-7f37-4cd5-b6aa-db35fe97ec7b.png)
