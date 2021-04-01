Screenshot for build complete:

![](build_complete.png)

Screenshot for experimental build test on cdash:

![](cdash_experimental.png)

Screenshot for error message after replacing the copyright file:

![](error_msg.png)

Fixing the error:
From the test output we know that the test case `25 - CMake.Copyright` failed. So I ran `ctest -I 25,25 -VV` to examine the test case in verbose mode. The output is:

![](test_25_error_msg.png)

Therefore I changed the year to be 2000-2021, and it worked:

![](test_25_success_msg.png)

CI on Github:
repo: https://github.com/Tyromancer/cmake-tutorial-CI
screenshot of success check:

![](pull_req.png)
