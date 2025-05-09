-- add_rules("mode.debug", "mode.release")
add_rules("mode.debug", "Print_Neatly","mode.release")
-- 设置target默认不构建
set_default(false)
-- 指定使用MSVC编译器
set_toolchains("msvc")
-- 为MSVC设置源文件编码为UTF-8
add_cxflags("/source-charset:utf-8", "/execution-charset:gbk")
-- if is_plat("windows") then
--     -- add_cxflags("/utf-8")
--     add_cxflags("/source-charset:utf-8", "/execution-charset:gbk")
-- end
rule("Print_Neatly")
    before_run(function (target)
        print("======================================================================")
        print("\x1b[32m".."[Before Run ReBuild]: Star!")
        print("\x1b[32m".."[  0%]: ".."\x1b[35m"..target:name())
        -- 重建当前target
        -- local ReBuild_Result = os.iorun("xmake -r "..target:name())
        -- 重建所有默认target
        -- local ReBuild_Result = os.iorun("xmake -r")
        -- printf(ReBuild_Result)
        print("\x1b[32m".."[Before Run ReBuild]: Over!")
        print("\x1b[0m".."======================================================================")
        print("\x1b[36m".."===================================[".."\x1b[35m"..target:name().."\x1b[36m"..": Target Star!]===================================")
    end)
    after_run(function (target) 
        print("===================================[".."\x1b[35m"..target:name().."\x1b[36m"..": Target Over!]===================================".."\x1b[0m")
    end)

target("Chapter2_CBasicConcepts")
    set_kind("binary")
    add_files("Chapter2_CBasicConcepts/*.c")
    add_files("Chapter2_CBasicConcepts/T2_Questions/*.c")
    set_default(true)

target("Test_Single")
    set_kind("binary")
    add_files("*.c")
    -- set_default(true)

--
-- If you want to known more usage about xmake, please see https://xmake.io
--
-- ## FAQ
--
-- You can enter the project directory firstly before building project.
--
--   $ cd projectdir
--
-- 1. How to build project?
--
--   $ xmake
--
-- 2. How to configure project?
--
--   $ xmake f -p [macosx|linux|iphoneos ..] -a [x86_64|i386|arm64 ..] -m [debug|release]
--
-- 3. Where is the build output directory?
--
--   The default output directory is `./build` and you can configure the output directory.
--
--   $ xmake f -o outputdir
--   $ xmake
--
-- 4. How to run and debug target after building project?
--
--   $ xmake run [targetname]
--   $ xmake run -d [targetname]
--
-- 5. How to install target to the system directory or other output directory?
--
--   $ xmake install
--   $ xmake install -o installdir
--
-- 6. Add some frequently-used compilation flags in xmake.lua
--
-- @code
--    -- add debug and release modes
--    add_rules("mode.debug", "mode.release")
--
--    -- add macro definition
--    add_defines("NDEBUG", "_GNU_SOURCE=1")
--
--    -- set warning all as error
--    set_warnings("all", "error")
--
--    -- set language: c99, c++11
--    set_languages("c99", "c++11")
--
--    -- set optimization: none, faster, fastest, smallest
--    set_optimize("fastest")
--
--    -- add include search directories
--    add_includedirs("/usr/include", "/usr/local/include")
--
--    -- add link libraries and search directories
--    add_links("tbox")
--    add_linkdirs("/usr/local/lib", "/usr/lib")
--
--    -- add system link libraries
--    add_syslinks("z", "pthread")
--
--    -- add compilation and link flags
--    add_cxflags("-stdnolib", "-fno-strict-aliasing")
--    add_ldflags("-L/usr/local/lib", "-lpthread", {force = true})
--
-- @endcode
--

