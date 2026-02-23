import re
from sendmail import mailman
from pwrd_automation import automation_check
import inputsrv
import hashlib


def hash_pwrd(pwrd):
    try:
        pwrd_hash = hashlib.sha1(str.encode(pwrd, 'utf-8')).hexdigest()
        print("HASHP: DONE")
        return pwrd_hash
    except:
        raise Exception(
            "something went wrong during hashing password operation.")


def regex(e, pwrd):
    pattern = re.compile(r'^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$')
    if re.fullmatch(pattern, e):
        print("RE: DONE!")
        result = automation_check(pwrd)
        hpwrd = hash_pwrd(pwrd)
        mailman(result, e, hpwrd)
    else:
        raise Exception("incorrect email format")
