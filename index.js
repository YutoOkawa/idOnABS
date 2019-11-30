var {PythonShell} = require('python-shell')

let option = {
    mode: 'json'
};

const absTrusteeSetup = (attributes) => {
    return new Promise((resolve,reject) => {
        var trusteeSetup = new PythonShell('trusteeSetup.py',option);
        var data = {
            'attr': attributes
        }
        trusteeSetup.send(data);
        trusteeSetup.on('message',function(data) {
            var tpk = data.tpk;
            resolve(tpk)
        })
    });
}

const absAuthoritySetup = (tpk,attributes) => {
    return new Promise((resolve,reject) => {
        var authoritySetup =  new PythonShell('authoritySetup.py',option);
        var data = {
            'tpk': tpk,
            'attr': attributes
        };
        authoritySetup.send(data);
        authoritySetup.on('message',function(data) {
            var key_list = data;
            resolve(key_list);
        });
    });
}

const absAttrgen = (key_list,attributes) => {
    return new Promise((resolve,reject) => {
        var attrgen = new PythonShell('attrgen.py',option);
        var ask = {
            "ask": key_list.ask,
            "attr": attributes
        };
        attrgen.send(ask);
        attrgen.on('message',function(data) {
            ska = data.ska;
            resolve(ska);
        });
    });
}

const absSign = (key_list,ska,message,policy,attributes) => {
    return new Promise((resolve,reject) => {
        var signgen = new PythonShell('sign.py',option);
        var signer = {
            "tpk":key_list.tpk,
            "apk":key_list.apk,
            "ska":ska,
            "message":message,
            "policy":policy,
            "attr": attributes
        };
        signgen.send(signer);
        signgen.on('message',function(data) {
            var sign = data.sign;
            resolve(sign);
        });
    });
}

const absVer = (key_list,sign,message,policy,attributes) => {
    return new Promise((resolve,reject) => {
        var verify = new PythonShell('ver.py',option);
        var verifier = {
            "tpk":key_list.tpk,
            "apk":key_list.apk,
            "sign":sign,
            "message":message,
            "policy":policy,
            "attr": attributes
        };
        verify.send(verifier);
        verify.on('message',function(data) {
            var bool = data.result;
            resolve(bool);
        });
    });
}

const absSystem = async() => {
    var userid = 'test'
    var attributes = 'CHIEF,SCHIEF,FRESHMAN,HRD,DD'
    var message = "message";
    var policy = "HRD OR SCHIEF";
    const tpk = await absTrusteeSetup(attributes);
    console.log('trustee ok');
    const key_list = await absAuthoritySetup(tpk,attributes);
    console.log("Setup Completed.")
    userid = userid.toUpperCase()
    attributes += ','+userid
    policy +=  ' AND ' + userid
    const ska = await absAttrgen(key_list,attributes);
    console.log("Key Generated.");
    const sign = await absSign(key_list,ska,message,policy,attributes);
    console.log("Sign Generated.");
    const ver = await absVer(key_list,sign,message,policy,attributes);
    if (ver) console.log("OK");
    else console.log("NG");
}

absSystem()
