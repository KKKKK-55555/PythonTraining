import pandas as pd


if __name__ == '__main__':
    # 各カテゴリの人数を定義
    data = [['group_a', 'Cat'], ['group_b', 'Dog'], ['group_a', 'Cat'], ['group_a', 'Cat'],
            ['group_b', 'Cat'], ['group_b', 'Dog'], ['group_b', 'Dog'], ['group_a', 'Cat'],
            ['group_a', 'Dog'], ['group_a', 'Dog'], ['group_b', 'Dog'], ['group_b', 'Cat'],
            ['group_b', 'Dog'], ['group_b', 'Cat'], ['group_a', 'Cat'], ['group_b', 'Cat'],
            ['group_b', 'Cat'], ['group_b', 'Cat'], ['group_a', 'Dog'], ['group_b', 'Cat'],
            ['group_a', 'Cat'], ['group_a', 'Cat'], ['group_b', 'Dog'], ['group_b', 'Dog'],
            ['group_b', 'Cat'], ['group_a', 'Cat'], ['group_b', 'Dog'], ['group_a', 'Cat'],
            ['group_b', 'Dog'], ['group_b', 'Dog'], ['group_a', 'Dog'], ['group_a', 'Cat'],
            ['group_a', 'Cat'], ['group_a', 'Cat'], ['group_b', 'Dog'], ['group_a', 'Dog'],
            ['group_b', 'Cat'], ['group_b', 'Dog'], ['group_b', 'Cat'], ['group_b', 'Cat'],
            ['group_b', 'Dog'], ['group_a', 'Dog'], ['group_a', 'Cat'], ['group_b', 'Dog'],
            ['group_a', 'Dog'], ['group_a', 'Cat'], ['group_a', 'Cat'], ['group_a', 'Cat'],
            ['group_b', 'Dog'], ['group_a', 'Cat']]
    
    # visualize
    df = pd.DataFrame(data,
                      columns=['Group', 'Preference'])

    print(pd.crosstab(df['Group'], df['Preference']))

