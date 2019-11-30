from MathABS import ABS
from charm.toolbox.pairinggroup import PairingGroup

def trusteeSetup(absinst,attributes):
    print('\nTrustee Setup')
    tpk = absinst.trusteesetup(attributes)
    print(tpk)
    return tpk

def authoritySetup(absinst,tpk,attributes):
    print('\nAuthority Setup')
    ask,apk = absinst.authoritysetup(tpk,attributes)
    print(ask)
    print(apk)
    return ask,apk

def attrGen(absinst,ask,attriList,attributes):
    print('\nAttrGen')
    ska = absinst.generateattributes(ask,attriList,attributes)
    print(ska)
    return ska

def sign(absinst,tpk,apk,ska,message,policy,attributes):
    print('\nSign')
    sign = absinst.sign((tpk,apk),ska,message,policy,attributes)
    print(sign)
    return sign

def verify(absinst,tpk,apk,sign,message,policy, attributes):
    print('\nVerify')
    print(absinst.verify((tpk,apk),sign,message,policy,attributes))

if __name__ == '__main__':
    userid = 'test'
    attributes = ['CHIEF','SCHIEF','FRESHMAN','HRD','DD']
    attriList = ['HRD']
    policy = 'HRD OR SCHIEF'
    message = 'message'
    group = PairingGroup('MNT159')
    absinst = ABS(group)

    # Trustee Setup
    tpk = trusteeSetup(absinst,attributes)

    # Authority Setup
    ask,apk = authoritySetup(absinst,tpk,attributes)

    userid = userid.upper()
    attributes.append(userid)
    attriList.append(userid)
    policy += ' AND ' + userid

    print(attributes)
    print(attriList)
    print(policy)

    # AttrGen
    ska = attrGen(absinst,ask,attriList,attributes)

    # Sign
    sign = sign(absinst,tpk,apk,ska,message,policy,attributes)

    # Verify
    verify(absinst,tpk,apk,sign,message,policy,attributes)
