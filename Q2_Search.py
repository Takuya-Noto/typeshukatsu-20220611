def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    # 探索範囲の始まりと終わりのインデックス
    start_index = 0
    end_index = len(sorted_array) - 1

    # 探索範囲がある限り繰り返す
    while (start_index <= end_index):
        # 探索範囲の中間のインデックス
        center_index = (start_index + end_index) // 2

        # 探索範囲の中間の値が探索対象と一致すれば、そのインデックスを返す
        if sorted_array[center_index] == target_number:
            return center_index

        # 探索範囲の中間の値が探索対象より大きければ、探索範囲の終わりのインデックスを更新
        elif sorted_array[center_index] > target_number:
            end_index = center_index - 1

        # 探索範囲の中間の値が探索対象より小さければ、探索範囲の始まりのインデックスを更新
        else:
            start_index = center_index + 1


    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()