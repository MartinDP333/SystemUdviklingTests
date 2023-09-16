import pytest
from television import Television

# Defines fixture to run pytest
@pytest.fixture
def tv():
    return Television()

# Tests if tv is on or off
def test_tvOnOff(tv): 
    assert not tv.on
    tv.tvOnOff()
    assert tv.on
    tv.tvOnOff()
    assert not tv.on
# Tests if channel up, down and get methods work
def test_channel(tv):
    initialChannel = tv.getCh()
    assert tv.getCh() == initialChannel
    tv.chUp()
    assert tv.getCh() == (initialChannel + 1)
    tv.chDown()
    assert tv.getCh() == initialChannel
# Tests if volume up, down and get methods work
def test_volume(tv):
    initialVolume = tv.getVol()
    assert tv.getVol() == initialVolume
    tv.volUp()
    assert tv.getVol() == (initialVolume + 2)
    tv.volDown()
    assert tv.getVol() == initialVolume
# Tests if mute and getMuted methods work
def test_mute(tv):
    assert not tv.getMuted()
    tv.muteOnOff()
    assert tv.getMuted()
    tv.muteOnOff()
    assert not tv.getMuted()

if __name__ == "__main__": # tells pytest to run if this is the main
    pytest.main()