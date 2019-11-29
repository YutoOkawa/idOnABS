from MathABS import ABS
from charm.toolbox.pairinggroup import PairingGroup

if __name__ == '__main__':
    userid = 'test'
    attributes = ['CHIEF','SCHIEF','FRESHMAN','HRD','DD']
    attriList = ['HRD']
    policy = 'HRD OR SCHIEF'
    group = PairingGroup('MNT159')
    absinst = ABS(group)

    # Trustee Setup
    print('\nTrustee Setup')
    tpk = absinst.trusteesetup(attributes)
    print(tpk)

    # Authority Setup
    print('\nAuthority Setup')
    ask,apk = absinst.authoritysetup(tpk,attributes)
    print(ask)
    print(apk)

    userid = userid.upper()
    attributes.append(userid)
    attriList.append(userid)
    policy += ' AND ' + userid

    print(attributes)
    print(attriList)
    print(policy)

    # AttrGen
    print('\nAttrGen')
    ska = absinst.generateattributes(ask,attriList,attributes)
    print(ska)

    # Sign
    print('\nSign')
    sign = absinst.sign((tpk,apk),ska,'message',policy,attributes)
    print(sign)

    # Verify
    print('\nVerify')
    print(absinst.verify((tpk,apk),sign,'message',policy,attributes))