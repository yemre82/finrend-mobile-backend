import pyotp
import hashlib


def check_otp(checked_otp):
    totp = pyotp.TOTP("JKFLSNVITJDNGVXS", digest=hashlib.sha1, interval=3600)
    if str(checked_otp)!=str(totp.now()):
        return "OTP is not True"
    return "OTP is True"
