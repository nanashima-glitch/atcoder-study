#B問題　花束
#問題URL　https://atcoder.jp/contests/arc050/tasks/arc050_b
#二分探索

import sys
#競プロで頻出 input より速い？

def main():

    R,B=map(int,input().split())
#map 入ってきた複数の文字をまとめてint(整数にして)にする
#split 分ける(,)の場合,が入ってくる
    x,y=map(int,input().split())

    low=0
    high=max(R,B)
    ans=0

    while low <= high:
        mid = (low + high) // 2

# mid 個の花束を作ることができるか判定
        # 1. そもそも合計で mid 本以上の赤と青があるか
        # 2. 各花束に最低1本ずつ割り振った後の「余り」で、追加で必要な本数(x-1, y-1)を賄えるか
        if R >= mid and B >= mid and ((R - mid) // (x - 1) + (B - mid) // (y - 1)) >= mid:
            ans = mid      # 作れるので現在の値を記録
            low = mid + 1  # もっと多くの個数を作れるか右側を探索
        else:
            high = mid - 1 # 作れないので個数を減らして左側を探索

    print(ans)

if __name__ == '__main__':
    main()
  
