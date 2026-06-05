from nodes import node1_acquisition, node2_feature, node3_anomaly, node4_classifier, node5_output

v, c = node1_acquisition.run()
p, r = node2_feature.run(v, c)
a = node3_anomaly.run(p)
s = node4_classifier.run(a)
out = node5_output.run(v, c, p, r, s)

print("OUTPUT:", out)