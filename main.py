import solve

token = solve.Altcha({
    "algorithm": "SHA-256",
    "challenge": "a5ba65be62c44edf66fac73912a5ebef199001a88ef1771fb77360381b5451df",
    "maxnumber": 10000,
    "salt": "863146992ac622ac3f7b0a30?edk=357c9445da9ecff83529b9f8e28a20b7&expires=1776371547&",
    "signature": "5ad5247cab841aef1b179b45e9f56d36e4e160ddcf5e4e335be2cb7137e60eb7"
})

print("token:", token)