class HocSinh:
    def __init__(self, ma, hoten, namsinh, gioitinh, van, toan, anh):
        self.ma = ma
        self.hoten = hoten
        self.namsinh = namsinh
        self.gioitinh = gioitinh
        self.van = int(van)
        self.toan = int(toan)
        self.anh = int(anh)

    def get_ten(self):
        return self.hoten.split()[-1]

    def get_ho(self):
        return " ".join(self.hoten.split()[:-1])

    def __str__(self):
        return f"{self.ma}|{self.hoten}|{self.namsinh}|{self.gioitinh}|{self.van}|{self.toan}|{self.anh}"


def cmp_key(hs: HocSinh):
    # sắp xếp: tên ↑, họ ↑, điểm toán ↓
    return (hs.get_ten(), hs.get_ho(), -hs.toan)


if __name__ == "__main__":
    n = int(input().strip())
    ds = []
    for _ in range(n):
        line = input().strip().split("|")
        hs = HocSinh(*line)
        ds.append(hs)

    ds.sort(key=cmp_key)

    for hs in ds:
        print(hs)
