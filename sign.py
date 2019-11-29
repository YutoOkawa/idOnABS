import sys,json
from MathABS import ABS
from charm.toolbox.pairinggroup import PairingGroup

def main():
    group = PairingGroup('MNT159')
    absinst = ABS(group)
    data = json.loads(sys.stdin.readline())
    tpk = absinst.decodestr(data['tpk'])
    apk = absinst.decodestr(data['apk'])
    ska = absinst.decodestr(data['ska'])
    message = data['message']
    policy = data['policy']
    attributes = data['attr'].split(',')
    lam = absinst.sign((tpk,apk),ska,message,policy,attributes)
    response = {"sign":absinst.encodestr(lam)}
    print(json.dumps(response))

if __name__ == "__main__":
    main()