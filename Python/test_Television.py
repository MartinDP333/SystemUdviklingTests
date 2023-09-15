import pytest
import math


on = False
channel = 0
volume = 0
mute = False

def test_tvOnOff():
    checkBool = on
    # Switch from on to off and vice versa
    assert on != checkBool
def test_chUp():
    assert channel > x
def test_chDown():
    assert channel < x
def test_getCh():
    channel = 5
    # Print number and check if it printed it
    assert out == channel
def test_volUp():
    assert vol > x
def test_volDown():
    assert vol < x
def test_getVol():
    assert out == volume
def test_mute():
    checkBool = mute
    assert mute != checkBool
def test_getMuted():
    assert out == mute
