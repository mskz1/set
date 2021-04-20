import subprocess

flag_make_one_dll = False
# flag_make_one_dll = True

ipyc_exe = r"C:\Program Files\IronPython 2.7\ipyc.exe"

src_files = ['/main:dummy_main.py', 'allowable_stress.py', 'bolt.py', 'rebar.py', 'xs_section.py']

if flag_make_one_dll:
    # １つのDLLにまとめることは可能なのか？
    # main_name = "/main:" + src_files[0]
    # src_files[0] = main_name
    print([ipyc_exe, r"/target:dll", *src_files])
    # res = subprocess.run([ipyc_exe, r"/target:dll", *src_files])
    res = subprocess.run([ipyc_exe, r"/target:dll", r"/out:xlset.dll", *src_files])

    # memo 2021-0312
    # 上記で、main　file の指定で、おかしなことにならないか？
    # 空の main_file を用意したほうがよいのか？
    # Target:ConsoleApplicationになって、拡張子は.dll とexeと両方できてる。main以外がdllになってるかも

else:
    for src_file in src_files:
        res = subprocess.run([ipyc_exe, r"/target:dll", src_file])
