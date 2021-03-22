#入力した文字列を反転し変換・出力するスクリプト
org_str = input("反転させたい文字列を入力してください:")
tmp_str_list = list(reversed(org_str))
rev_str = ''.join(tmp_str_list)
print(rev_str)