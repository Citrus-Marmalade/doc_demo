===================
CPC MIMXRT595S Port
===================
This NXP port offers CPC SDIO and SPI driver implementations specific for the development board `MIMXRT595-EVK <https://www.nxp.com/design/design-center/development-boards-and-designs/i-mx-evaluation-and-development-boards/i-mx-rt595-evaluation-kit:MIMXRT595-EVK>`_. The SDIO driver leverages NXP's high-level SDIO API provided by the SDK, while the SPI driver utilizes the CMSIS API included in the NXP SDK.

Getting Started
===============
1. Download NXP's SDK. 
2. Hardware
3. Generate the test project
4. Flash the device. 

1. Download NXP's SDK
---------------------
Clone NXP's mcux-sdk repository by executing the commands below. 

.. parsed-literal::
    $ west init -m https://github.com/NXPmicro/mcux-sdk --mr ${revision} mcuxsdk
    $ cd mcuxsdk
    $ west update

NXP's Github page `here <https://github.com/nxp-mcuxpresso/mcux-sdk>`_.


2. Hardware
-----------
.. Attention::

   The EVK board only supports a voltage of 1.8V. Ensure that any device you want to interface with the EVK board is also aligned to this voltage level to avoid damage or malfunction.

.. caution::

   Users who want to use the SDIO will need to make some modifications to the hardware. For more information, please refer to the SDIO tabs below.


The NXP EVK board is designed for developers to prototype and test their applications on NXP microcontrollers. It includes various peripherals and interfaces to facilitate development and debugging. The CPC SDIO and SPI driver were developped using this Evaluation Kit. 



.. image:: assets/NXP_EVK_board.png
   :alt: NXP EVK Board


.. tab-set::
   .. tab-item:: SPI

      The SPI driver utilizes the High SPI interface available on the EVK board at JP26. Users can find the CS, CLK, MISO, MOSI, and ground pins on this jumper. Additionally, the SPI requires a flow control pin from the secondary device. The secondary device signals the primary driver that data is ready via Pin 1 on Jumper 30.

      *SPI Pin Mapping Table*

      =======  =======  =======
      Signal   Jumper   Pin
      =======  =======  =======
      CS       JP26     1
      CLK      JP26     4
      MISO     JP26     2
      MOSI     JP26     3
      GND      JP26     5
      IRQ Pin  JP30     1
      =======  =======  =======

      *Refer to the image shown below to locate the jumpers*

   .. tab-item:: SDIO
      
      **Re-route SDIO line**

      The MIMXRT595-EVK board includes an SD card slot, but the SDIO lines are routed to an onboard eMMC module by default. To enable SDIO communication with an SD card, you must re-route the lines as described below.

      *Resistor Population Table*

      ========  ============================  ===========================
      Device    Resistors to Populate         Resistors to DNP
      ========  ============================  ===========================
      SD Card   R691~R697                     R611~R620, R660, R661, R698
      eMMC      R611~R620, R660, R661, R698   R691~R697
      ========  ============================  ===========================

      **SDIO Card adaptor Vcc**  

      Hardware modifications were made to the EVK board to address voltage compatibility issues. The MIMXRT595-EVK board supplies 1.8V for SDIO communication lines but does not support 3.3V signaling for these lines. However, the SD card slot provides 3.3V to the card's VCC pin, which cannot be switched to 1.8V. This mismatch creates a potential compatibility issue for SDIO cards requiring uniform voltage levels for both VCC and IO lines. Altough, in a "real" Everest chip environment, this will not be an issue since the hardware is designed to properly handle 3.3V signaling on the SDIO lines. For now, these modifications are required to ensure stable operation in the FPGA test configuration


      *The EVK board supplies only 1.8V to the SDIO lines, making the board incompatible with SDIO v2.0 and lower*

3. Generate the Test Project
----------------------------
To generate the project, use **CMake** with the following command:

.. parsed-literal::
   $ cmake -DMCUX_SDK_DIR:PATH=<PATH_TO_MCUX_SDK> \
         -DCMAKE_TOOLCHAIN_FILE:FILEPATH=<gsdk/platform/service/cpc-v2/test/port/nxp/evkmimxrt595/armgcc.cmake> \
         -DCMAKE_BUILD_TYPE=Debug \
         -S<PATH_TO_GSDK>
    

Once the project is generated, navigate to the build folder and compile the project using:

.. parsed-literal::
   $ make


4. Flash the Device
-------------------
Use J-Link and GDB to flash the firmware and debug the application:

1. Connect the EVK board to your PC via USB using the onboard J-Link debugger. (J40)
2. Flash the firmware using GDB.