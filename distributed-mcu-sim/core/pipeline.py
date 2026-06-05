from nodes import acquisition, feature, anomaly, classifier
from core.metrics import Metrics
from monitoring.logger import log

metrics = Metrics()

def run():
    metrics.start_timer()

    v,c = acquisition.process(None)
    v,c,p,r = feature.process((v,c))
    v,c,p,r,status = anomaly.process((v,c,p,r))
    v,c,p,r,status = classifier.process((v,c,p,r,status))

    metrics.end_timer()

    log(v,c,p,r,status)

    return (v,c,p,r,status), metrics