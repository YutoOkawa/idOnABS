import sys,json
from MathABS import ABS
from charm.toolbox.pairinggroup import PairingGroup

def main():
    group = PairingGroup('MNT159')
    absinst = ABS(group)
    data = json.loads(sys.stdin.readline())
    tpk = absinst.decodestr(data['tpk'])
    attributes = data['attr'].split(',')
    ask,apk = absinst.authoritysetup(tpk,attributes)
    response = {
        "tpk":absinst.encodestr(tpk),
        "ask":absinst.encodestr(ask),
        "apk":absinst.encodestr(apk)
    }
    print(json.dumps(response))

if __name__ == "__main__":
    main()