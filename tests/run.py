# from tests import test as Test
from tests import test
# from code_wars.strings_mix import mix
#
# Test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
# Test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
# Test.assert_equals(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
# Test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
# Test.assert_equals(mix("codewars", "codewars"), "")
# Test.assert_equals(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")

from code_wars.greed_is_good import score
test.assert_equals( score( [2, 3, 4, 6, 2] ), 0)
test.assert_equals( score(  [4, 4, 4, 3, 3] ), 400)
test.assert_equals( score(  [2, 4, 4, 5, 4] ), 450)
test.assert_equals( score(  [1, 1, 1, 3, 1] ), 1100)