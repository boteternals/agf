import base64, marshal, zlib, os

def cenan_encrypt(plain_code):
    bytecode = marshal.dumps(compile(plain_code, '<agf_internal>', 'exec'))
    compressed = zlib.compress(bytecode)
    encoded = base64.b64encode(compressed).decode('utf-8')
    return f'import base64, marshal, zlib; exec(marshal.loads(zlib.decompress(base64.b64decode("{encoded}"))))'

targets = ['agf/provider.py', 'agf/bridge.py', 'agf/core.py', 'agf/hf_provider.py']

for target in targets:
    if os.path.exists(target):
        with open(target, 'r') as f:
            code = f.read()
        if "base64.b64decode" not in code:
            with open(target, 'w') as f:
                f.write(f"# Encrypted by Cenan (Eternals Edition)\n{cenan_encrypt(code)}")
            print(f"[*] {target} Encrypted.")

print("\n>>> [SUCCESS] AGF Library is now protected and ready to install.")

