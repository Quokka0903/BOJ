W, H = map(int, input().split())
X, Y = map(int, input().split())
T = int(input())

# 사분면 안에서 이동하는 것으로 생각하지 말고, 
# 전체 이동거리만큼 사분면이 확장되었다고 생각하는 게 빠르다.

X = (X + T) % (W * 2) if (X + T) % (W * 2) < W else (W * 2) - (X + T) % (W * 2)
# X가 W의 두 배라면 X가 원위치인 것. 
# X가 W보다 작다면 증가하는 과정. 
# X가 W보다 크다면 한번 튕기고 적어지는 과정.

Y = (Y + T) % (H * 2) if (Y + T) % (H * 2) < H else (H * 2) - (Y + T) % (H * 2)
# 위와 같은 방식이다.

print (f'{X} {Y}')