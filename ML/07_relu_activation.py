def relu(xs):
   return [max(0, x) for x in xs]

if __name__ == "__main__":
    print(relu(list(map(int, (input("nhập mảng: ").split())))))
