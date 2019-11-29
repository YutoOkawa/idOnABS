from MathABS import ABS
from charm.toolbox.pairinggroup import PairingGroup

if __name__ == '__main__':
    attributes = ['CHIEF','SCHIEF','FRESHMAN','HRD','DD']
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

    # AttrGen
    print('\nAttrGen')
    ska = absinst.generateattributes(ask,['HRD','SCHIEF'],attributes)
    print(ska)

    # Sign
    print('\nSign')
    sign = absinst.sign((tpk,apk),ska,'message','HRD AND SCHIEF',attributes)
    print(sign)

    # Verify
    print('\nVerify')
    print(absinst.verify((tpk,apk),sign,'message','HRD AND SCHIEF',attributes))