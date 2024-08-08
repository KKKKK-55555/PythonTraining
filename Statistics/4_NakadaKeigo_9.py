import pandas as pd
from scipy.stats import chi2_contingency


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

    cross_table = pd.crosstab(df['Group'], df['Preference'])
    print(cross_table)

    # chi test
    chi2, p, dof, expected = chi2_contingency(cross_table)
    print(f'chi2: {chi2}')
    print(f'p: {p}')
    print(f'dof: {dof}')
    print(f'expected: {expected}')
