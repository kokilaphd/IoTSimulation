#! /usr/bin/env python

# Programs that are runnable.
ns3_runnable_programs = ['build/src/aodv/examples/ns3.25-aodv-debug', 'build/src/bridge/examples/ns3.25-csma-bridge-debug', 'build/src/bridge/examples/ns3.25-csma-bridge-one-hop-debug', 'build/src/brite/examples/ns3.25-brite-generic-example-debug', 'build/src/brite/examples/ns3.25-brite-MPI-example-debug', 'build/src/buildings/examples/ns3.25-buildings-pathloss-profiler-debug', 'build/src/config-store/examples/ns3.25-config-store-save-debug', 'build/src/core/examples/ns3.25-main-callback-debug', 'build/src/core/examples/ns3.25-sample-simulator-debug', 'build/src/core/examples/ns3.25-main-ptr-debug', 'build/src/core/examples/ns3.25-main-random-variable-debug', 'build/src/core/examples/ns3.25-main-random-variable-stream-debug', 'build/src/core/examples/ns3.25-sample-random-variable-debug', 'build/src/core/examples/ns3.25-sample-random-variable-stream-debug', 'build/src/core/examples/ns3.25-command-line-example-debug', 'build/src/core/examples/ns3.25-hash-example-debug', 'build/src/core/examples/ns3.25-main-test-sync-debug', 'build/src/csma/examples/ns3.25-csma-one-subnet-debug', 'build/src/csma/examples/ns3.25-csma-broadcast-debug', 'build/src/csma/examples/ns3.25-csma-packet-socket-debug', 'build/src/csma/examples/ns3.25-csma-multicast-debug', 'build/src/csma/examples/ns3.25-csma-raw-ip-socket-debug', 'build/src/csma/examples/ns3.25-csma-ping-debug', 'build/src/csma-layout/examples/ns3.25-csma-star-debug', 'build/src/dsdv/examples/ns3.25-dsdv-manet-debug', 'build/src/dsr/examples/ns3.25-dsr-debug', 'build/src/energy/examples/ns3.25-li-ion-energy-source-debug', 'build/src/energy/examples/ns3.25-rv-battery-model-test-debug', 'build/src/energy/examples/ns3.25-basic-energy-model-test-debug', 'build/src/fd-net-device/examples/ns3.25-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.25-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.25-realtime-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.25-realtime-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.25-fd-emu-ping-debug', 'build/src/fd-net-device/examples/ns3.25-fd-emu-udp-echo-debug', 'build/src/fd-net-device/examples/ns3.25-fd-emu-onoff-debug', 'build/src/fd-net-device/examples/ns3.25-fd-tap-ping-debug', 'build/src/fd-net-device/examples/ns3.25-fd-tap-ping6-debug', 'build/src/internet/examples/ns3.25-main-simple-debug', 'build/src/lr-wpan/examples/ns3.25-lr-wpan-packet-print-debug', 'build/src/lr-wpan/examples/ns3.25-lr-wpan-phy-test-debug', 'build/src/lr-wpan/examples/ns3.25-lr-wpan-data-debug', 'build/src/lr-wpan/examples/ns3.25-lr-wpan-error-model-plot-debug', 'build/src/lr-wpan/examples/ns3.25-lr-wpan-error-distance-plot-debug', 'build/src/lte/examples/ns3.25-lena-cqi-threshold-debug', 'build/src/lte/examples/ns3.25-lena-dual-stripe-debug', 'build/src/lte/examples/ns3.25-lena-fading-debug', 'build/src/lte/examples/ns3.25-lena-intercell-interference-debug', 'build/src/lte/examples/ns3.25-lena-pathloss-traces-debug', 'build/src/lte/examples/ns3.25-lena-profiling-debug', 'build/src/lte/examples/ns3.25-lena-rem-debug', 'build/src/lte/examples/ns3.25-lena-rem-sector-antenna-debug', 'build/src/lte/examples/ns3.25-lena-rlc-traces-debug', 'build/src/lte/examples/ns3.25-lena-simple-debug', 'build/src/lte/examples/ns3.25-lena-simple-epc-debug', 'build/src/lte/examples/ns3.25-lena-deactivate-bearer-debug', 'build/src/lte/examples/ns3.25-lena-x2-handover-debug', 'build/src/lte/examples/ns3.25-lena-x2-handover-measures-debug', 'build/src/lte/examples/ns3.25-lena-frequency-reuse-debug', 'build/src/lte/examples/ns3.25-lena-distributed-ffr-debug', 'build/src/lte/examples/ns3.25-lena-uplink-power-control-debug', 'build/src/mesh/examples/ns3.25-mesh-debug', 'build/src/mobility/examples/ns3.25-main-grid-topology-debug', 'build/src/mobility/examples/ns3.25-main-random-topology-debug', 'build/src/mobility/examples/ns3.25-main-random-walk-debug', 'build/src/mobility/examples/ns3.25-mobility-trace-example-debug', 'build/src/mobility/examples/ns3.25-ns2-mobility-trace-debug', 'build/src/mobility/examples/ns3.25-bonnmotion-ns2-example-debug', 'build/src/mpi/examples/ns3.25-simple-distributed-debug', 'build/src/mpi/examples/ns3.25-third-distributed-debug', 'build/src/mpi/examples/ns3.25-nms-p2p-nix-distributed-debug', 'build/src/mpi/examples/ns3.25-simple-distributed-empty-node-debug', 'build/src/netanim/examples/ns3.25-dumbbell-animation-debug', 'build/src/netanim/examples/ns3.25-grid-animation-debug', 'build/src/netanim/examples/ns3.25-star-animation-debug', 'build/src/netanim/examples/ns3.25-wireless-animation-debug', 'build/src/netanim/examples/ns3.25-uan-animation-debug', 'build/src/netanim/examples/ns3.25-colors-link-description-debug', 'build/src/netanim/examples/ns3.25-resources-counters-debug', 'build/src/network/examples/ns3.25-main-packet-header-debug', 'build/src/network/examples/ns3.25-main-packet-tag-debug', 'build/src/network/examples/ns3.25-packet-socket-apps-debug', 'build/src/nix-vector-routing/examples/ns3.25-nix-simple-debug', 'build/src/nix-vector-routing/examples/ns3.25-nms-p2p-nix-debug', 'build/src/olsr/examples/ns3.25-simple-point-to-point-olsr-debug', 'build/src/olsr/examples/ns3.25-olsr-hna-debug', 'build/src/point-to-point/examples/ns3.25-main-attribute-value-debug', 'build/src/propagation/examples/ns3.25-main-propagation-loss-debug', 'build/src/propagation/examples/ns3.25-jakes-propagation-model-example-debug', 'build/src/sixlowpan/examples/ns3.25-example-sixlowpan-debug', 'build/src/sixlowpan/examples/ns3.25-example-ping-lr-wpan-debug', 'build/src/spectrum/examples/ns3.25-adhoc-aloha-ideal-phy-debug', 'build/src/spectrum/examples/ns3.25-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-debug', 'build/src/spectrum/examples/ns3.25-adhoc-aloha-ideal-phy-with-microwave-oven-debug', 'build/src/spectrum/examples/ns3.25-tv-trans-example-debug', 'build/src/spectrum/examples/ns3.25-tv-trans-regional-example-debug', 'build/src/stats/examples/ns3.25-gnuplot-example-debug', 'build/src/stats/examples/ns3.25-double-probe-example-debug', 'build/src/stats/examples/ns3.25-time-probe-example-debug', 'build/src/stats/examples/ns3.25-gnuplot-aggregator-example-debug', 'build/src/stats/examples/ns3.25-gnuplot-helper-example-debug', 'build/src/stats/examples/ns3.25-file-aggregator-example-debug', 'build/src/stats/examples/ns3.25-file-helper-example-debug', 'build/src/tap-bridge/examples/ns3.25-tap-csma-debug', 'build/src/tap-bridge/examples/ns3.25-tap-csma-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.25-tap-wifi-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.25-tap-wifi-dumbbell-debug', 'build/src/topology-read/examples/ns3.25-topology-example-sim-debug', 'build/src/traffic-control/examples/ns3.25-red-tests-debug', 'build/src/traffic-control/examples/ns3.25-red-vs-ared-debug', 'build/src/traffic-control/examples/ns3.25-adaptive-red-tests-debug', 'build/src/traffic-control/examples/ns3.25-pfifo-vs-red-debug', 'build/src/traffic-control/examples/ns3.25-codel-vs-pfifo-basic-test-debug', 'build/src/traffic-control/examples/ns3.25-codel-vs-pfifo-asymmetric-debug', 'build/src/uan/examples/ns3.25-uan-cw-example-debug', 'build/src/uan/examples/ns3.25-uan-rc-example-debug', 'build/src/virtual-net-device/examples/ns3.25-virtual-net-device-debug', 'build/src/wave/examples/ns3.25-wave-simple-80211p-debug', 'build/src/wave/examples/ns3.25-wave-simple-device-debug', 'build/src/wave/examples/ns3.25-vanet-routing-compare-debug', 'build/src/wifi/examples/ns3.25-wifi-phy-test-debug', 'build/src/wifi/examples/ns3.25-test-interference-helper-debug', 'build/src/wifi/examples/ns3.25-ideal-wifi-manager-example-debug', 'build/src/wifi/examples/ns3.25-minstrel-ht-wifi-manager-example-debug', 'build/src/wimax/examples/ns3.25-wimax-ipv4-debug', 'build/src/wimax/examples/ns3.25-wimax-multicast-debug', 'build/src/wimax/examples/ns3.25-wimax-simple-debug', 'build/examples/udp-client-server/ns3.25-udp-client-server-debug', 'build/examples/udp-client-server/ns3.25-udp-trace-client-server-debug', 'build/examples/socket/ns3.25-socket-bound-static-routing-debug', 'build/examples/socket/ns3.25-socket-bound-tcp-static-routing-debug', 'build/examples/socket/ns3.25-socket-options-ipv4-debug', 'build/examples/socket/ns3.25-socket-options-ipv6-debug', 'build/examples/udp/ns3.25-udp-echo-debug', 'build/examples/stats/ns3.25-wifi-example-sim-debug', 'build/examples/realtime/ns3.25-realtime-udp-echo-debug', 'build/examples/error-model/ns3.25-simple-error-model-debug', 'build/examples/wireless/ns3.25-mixed-wireless-debug', 'build/examples/wireless/ns3.25-wifi-adhoc-debug', 'build/examples/wireless/ns3.25-wifi-clear-channel-cmu-debug', 'build/examples/wireless/ns3.25-wifi-ap-debug', 'build/examples/wireless/ns3.25-wifi-wired-bridging-debug', 'build/examples/wireless/ns3.25-multirate-debug', 'build/examples/wireless/ns3.25-wifi-simple-adhoc-debug', 'build/examples/wireless/ns3.25-wifi-simple-adhoc-grid-debug', 'build/examples/wireless/ns3.25-wifi-simple-infra-debug', 'build/examples/wireless/ns3.25-wifi-simple-interference-debug', 'build/examples/wireless/ns3.25-wifi-blockack-debug', 'build/examples/wireless/ns3.25-ofdm-validation-debug', 'build/examples/wireless/ns3.25-ofdm-ht-validation-debug', 'build/examples/wireless/ns3.25-ofdm-vht-validation-debug', 'build/examples/wireless/ns3.25-wifi-hidden-terminal-debug', 'build/examples/wireless/ns3.25-ht-wifi-network-debug', 'build/examples/wireless/ns3.25-vht-wifi-network-debug', 'build/examples/wireless/ns3.25-wifi-timing-attributes-debug', 'build/examples/wireless/ns3.25-wifi-sleep-debug', 'build/examples/wireless/ns3.25-power-adaptation-distance-debug', 'build/examples/wireless/ns3.25-power-adaptation-interference-debug', 'build/examples/wireless/ns3.25-rate-adaptation-distance-debug', 'build/examples/wireless/ns3.25-wifi-aggregation-debug', 'build/examples/wireless/ns3.25-simple-ht-hidden-stations-debug', 'build/examples/wireless/ns3.25-80211n-mimo-debug', 'build/examples/wireless/ns3.25-mixed-bg-network-debug', 'build/examples/wireless/ns3.25-wifi-tcp-debug', 'build/examples/naming/ns3.25-object-names-debug', 'build/examples/tutorial/ns3.25-hello-simulator-debug', 'build/examples/tutorial/ns3.25-first-debug', 'build/examples/tutorial/ns3.25-second-debug', 'build/examples/tutorial/ns3.25-third-debug', 'build/examples/tutorial/ns3.25-fourth-debug', 'build/examples/tutorial/ns3.25-fifth-debug', 'build/examples/tutorial/ns3.25-sixth-debug', 'build/examples/tutorial/ns3.25-seventh-debug', 'build/examples/routing/ns3.25-dynamic-global-routing-debug', 'build/examples/routing/ns3.25-static-routing-slash32-debug', 'build/examples/routing/ns3.25-global-routing-slash32-debug', 'build/examples/routing/ns3.25-global-injection-slash32-debug', 'build/examples/routing/ns3.25-simple-global-routing-debug', 'build/examples/routing/ns3.25-simple-alternate-routing-debug', 'build/examples/routing/ns3.25-mixed-global-routing-debug', 'build/examples/routing/ns3.25-simple-routing-ping6-debug', 'build/examples/routing/ns3.25-manet-routing-compare-debug', 'build/examples/routing/ns3.25-ripng-simple-network-debug', 'build/examples/routing/ns3.25-rip-simple-network-debug', 'build/examples/routing/ns3.25-global-routing-multi-switch-plus-router-debug', 'build/examples/ipv6/ns3.25-icmpv6-redirect-debug', 'build/examples/ipv6/ns3.25-ping6-debug', 'build/examples/ipv6/ns3.25-radvd-debug', 'build/examples/ipv6/ns3.25-radvd-two-prefix-debug', 'build/examples/ipv6/ns3.25-test-ipv6-debug', 'build/examples/ipv6/ns3.25-fragmentation-ipv6-debug', 'build/examples/ipv6/ns3.25-fragmentation-ipv6-two-MTU-debug', 'build/examples/ipv6/ns3.25-loose-routing-ipv6-debug', 'build/examples/ipv6/ns3.25-wsn-ping6-debug', 'build/examples/traffic-control/ns3.25-traffic-control-debug', 'build/examples/tcp/ns3.25-tcp-large-transfer-debug', 'build/examples/tcp/ns3.25-tcp-nsc-lfn-debug', 'build/examples/tcp/ns3.25-tcp-nsc-zoo-debug', 'build/examples/tcp/ns3.25-tcp-star-server-debug', 'build/examples/tcp/ns3.25-star-debug', 'build/examples/tcp/ns3.25-tcp-bulk-send-debug', 'build/examples/tcp/ns3.25-tcp-pcap-nanosec-example-debug', 'build/examples/tcp/ns3.25-tcp-nsc-comparison-debug', 'build/examples/tcp/ns3.25-tcp-variants-comparison-debug', 'build/examples/energy/ns3.25-energy-model-example-debug', 'build/examples/energy/ns3.25-energy-model-with-harvesting-example-debug', 'build/examples/matrix-topology/ns3.25-matrix-topology-debug', 'build/scratch/ns3.25-try3-debug', 'build/scratch/ns3.25-scratch-simulator-debug', 'build/scratch/ns3.25-first1-debug', 'build/scratch/ns3.25-iot-debug', 'build/scratch/ns3.25-first-debug', 'build/scratch/subdir/ns3.25-subdir-debug', 'build/scratch/ns3.25-try-debug', 'build/scratch/ns3.25-try2-debug', 'build/scratch/ns3.25-myfirst-debug']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'realtime-udp-echo.py', 'mixed-wireless.py', 'wifi-ap.py', 'first.py', 'second.py', 'third.py', 'simple-routing-ping6.py']

