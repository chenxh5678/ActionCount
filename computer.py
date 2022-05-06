import math

'''计算角度'''
def cal_angle(pA, pB, pC, pD):  # pA（x,y,z)上端中，pB上端远，pC下端中，pD下端远
    a_x, b_x, c_x, d_x = pA[0], pB[0], pC[0], pD[0]  # 点a、b、c、d的x坐标
    a_y, b_y, c_y, d_y = pA[1], pB[1], pC[1], pD[1]  # 点a、b、c、d的y坐标

    if len(pA) == len(pB) == len(pC) == len(pD)== 3:
        a_z, b_z, c_z, d_z = pA[2], pB[2], pC[2], pD[2]  # 点a、b、c、d的z坐标
    else:
        a_z, b_z, c_z, d_z = 0,0,0,0  # 坐标点为2维坐标形式，z 坐标默认值设为0
        
    # 向量 m=(x1,y1,z1), n=(x2,y2,z2)
    x1,y1,z1 = (b_x-a_x),(b_y-a_y),(b_z-a_z)
    x2,y2,z2 = (d_x-c_x),(d_y-c_y),(d_z-c_z)

    # 两个向量的夹角，即角点b的夹角余弦值
    cos_b = (x1*x2 + y1*y2 + z1*z2) / (math.sqrt(x1**2 + y1**2 + z1**2) *(math.sqrt(x2**2 + y2**2 + z2**2))) # 角点b的夹角余弦值
    B = math.degrees(math.acos(cos_b)) # 角点b的夹角值
    return B


# a = cal_angle((1,1), (0,0), (1,0), (2,0))  # 结果为 45°
# print(a)



