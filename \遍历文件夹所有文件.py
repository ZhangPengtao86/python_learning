#/usr/bin/env python
import os
for top_dir, sub_dir, files in os.walk(os.getcwd()):
        for fi in files:
                print os.path.join(top_dir, fi)




#输出：
/root/dcp_test/Beta/fpga-internal/rtl/simple_afu/simple_app.cpp
/root/dcp_test/Beta/bin/packager
/root/dcp_test/Beta/bin/clean.sh
/root/dcp_test/Beta/bin/run.sh
/root/dcp_test/Beta/opencl/hello_world.aocx
/root/dcp_test/Beta/opencl/exm_opencl_hello_world_x64_linux.tgz
/root/dcp_test/Beta/opencl/vector_add.aocx
/root/dcp_test/Beta/opencl/exm_opencl_vector_add_x64_linux.tgz
/root/dcp_test/Beta/opencl/opencl_bsp.tar.gz
/root/dcp_test/tools/packager/packager.pyz
/root/dcp_test/bin/packager
/root/dcp_test/bin/clean.sh
