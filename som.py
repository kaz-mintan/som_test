#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'emoson'
#ユークリッド距離
dist = lambda vec1, vec2: (sum([(vec[0]-vec[1])**2 for vec in list(zip(vec1, vec2))]))**0.5

def near(map_vector, input_vector):
    """
    input_vectorに対し、最近傍ユニットのラベルを返す
    :param map_vector:
    :param input_vector:
    :return:
    """
    dist_vector = [dist(input_vector, m) for m in map_vector]
    return dist_vector.index(min(dist_vector))


def learning(input_vectors, map_width, map_height, vec_size, learning_count, area_size):
    """
    自己組織化マップの学習
    :param input_vectors:
    :param map_width:
    :param map_height:
    :param vec_size 入力ベクトルの次元数(色の場合はrgbの3次元):
    :param learning_count:
    :param area_size:
    :return map_vector:
    """
    import random
    map_vector = [[random.random() for v in range(vec_size)] for h in range(map_height) for w in range(map_width)]
    a = 1.0
    a_size = area_size
    for t in range(learning_count):
        for input_vector in input_vectors:
            #近傍ユニットの探索
            bmu = near(map_vector=map_vector, input_vector=input_vector)
            #重みの更新
            for i in range(map_width * map_height):
                c = (a_size - dist([i // map_width, i % map_width], [bmu // map_width, bmu % map_width]))
                if c > 0:
                    map_vector[i] = [mv+c*a*(iv-mv) for iv, mv in zip(input_vector, map_vector[i])]
        #学習係数、学習範囲の更新
        a = (learning_count - t) / learning_count
        a_size = area_size * (learning_count - t) / learning_count
    return map_vector

width = 20
height = 20
import random
input_vectors = [[random.random() for j in range(3)] for i in range(30)]
som_map = learning(input_vectors=input_vectors, map_width=width, map_height=height, vec_size=3, learning_count=0, area_size=3)
