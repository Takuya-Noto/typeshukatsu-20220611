def main():
    # ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array) -> list:
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    si = 0
    ei = len(array) - 1

    while(True):
        # 順方向に探索
        # 逆方向の探索のインデックスに出会うまで
        for i in range(si, ei):
            # 基準値以上の値のインデックスを取得
            if array[i] >= pivot:
                si = i
                break

            # 逆方向の探索と出会ったら配列を分割し、それぞれを引数として関数を再帰的に呼び出す
            if i == ei-1:
                return sort(array[:ei]) + sort(array[ei:])

        # 逆方向の探索
        # 順方向の探索のインデックスに出会うまで
        for j in range(ei, si, -1):
            # 基準値未満の値のインデックスを取得
            if array[j] < pivot:
                ei = j
                break

            # 順方向の探索と出会ったら配列を分割し、それぞれを引数として関数を再帰的に呼び出す
            if j == si+1:
                # 一度も交換が起きていない時は、分割の仕方を変える
                if si == 0:
                    return sort(array[:1]) + sort(array[1:])
                else:
                    return sort(array[:si]) + sort(array[si:])

        # 取得したインデックスに対応する値を交換
        tmp = array[si]
        array[si] = array[ei]
        array[ei] = tmp


    # ここまで記述

if __name__ == '__main__':
    main()