#!/usr/bin/python3
import sys
import math

def matrix_product(matrix_a, matrix_b):
    result_matrix = [[0 for i in range(len(matrix_b[0]))] for i in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_a[0])):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result_matrix

def translation_transform(i , j):
    return [
    [1, 0, i],
    [0, 1, j],
    [0, 0, 1]
    ]

def scaling_transform(m, n):
    return [
        [m, 0, 0],
        [0, n, 0],
        [0, 0, 1]
    ]

def rotation_transform(d):
    return [
        [math.cos(d * (math.pi / 180)), -math.sin(d * (math.pi / 180)), 0],
        [math.sin(d * (math.pi / 180)), math.cos(d * (math.pi / 180)), 0],
        [0, 0, 1]
    ]

def reflection_transform(d):
    matrix_1 = [
        [math.cos(d * math.pi / 180), math.sin(d * math.pi / 180), 0],
        [-math.sin(d * math.pi / 180), math.cos(d * math.pi / 180), 0],
        [0, 0, 1]
    ]

    matrix_2 = [
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ]

    matrix_3 = [
        [math.cos(d * math.pi / 180), -math.sin(d * math.pi / 180), 0],
        [math.sin(d * math.pi / 180), math.cos(d * math.pi / 180), 0],
        [0, 0, 1]
    ]

    return matrix_product(matrix_product(matrix_1, matrix_2), matrix_3)

args = sys.argv

x = float(args[1])
y = float(args[2])
w = 1
point = [[x * w], [y * w], [w]]


i = 3
matrix_list = []
nb_args = len(args)
display_instruction_list = []

while (i < nb_args):
    if (args[i] == "-t"):
        if (i + 2 < nb_args):
            matrix_list.append(translation_transform(int(args[i + 1]), int(args[i + 2])))
            display_instruction_list.append("Translation along vector ({}, {})".format(args[i + 1], args[i + 2]))
            i += 3
    elif (args[i] == "-z"):
        if (i + 2< nb_args):
            matrix_list.append(scaling_transform(int(args[i + 1]), int(args[i + 2])))
            display_instruction_list.append("Scaling by factors {} and {}".format(args[i + 1], args[i + 2]))
            i += 3
    elif (args[i] == "-r"):
        if (i + 1 < nb_args):
            matrix_list.append(rotation_transform(int(args[i + 1])))
            display_instruction_list.append("Rotation by a {} degree angle".format(args[i + 1]))
            i += 2
    elif (args[i] == "-s"):
        if (i + 1 < nb_args):
            matrix_list.append(reflection_transform(int(args[i + 1])))
            display_instruction_list.append("Reflection over an axis with an inclination angle of {} degrees".format(args[i + 1]))
            i += 2

matrix_result = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

for element in matrix_list:
    matrix_result = matrix_product(matrix_result, element)

for element in display_instruction_list:
    print(element)

for row in matrix_result:
    for value in row:
        print("{:.2f}".format(value), "\t", end='')
    print("")

multiplied_point = matrix_product(matrix_result, point)

print("({:.2f}, {:.2f}) => ({:.2f}, {:.2f})".format(float(args[1]), float(args[2]), multiplied_point[0][0], multiplied_point[1][0]))

exit(0)