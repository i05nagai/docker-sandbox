package org.example.operators

import org.apache.flink.api.common.functions.RichMapFunction
import org.apache.flink.configuration.Configuration
import org.apache.flink.metrics.Counter

class SampleCounterMetricMap extends RichMapFunction[String,String] {
  @transient private var counter: Counter = _

  override def open(parameters: Configuration): Unit = {
    counter = getRuntimeContext()
      .getMetricGroup()
      .counter("SampleCounterMetric")
  }

  override def map(value: String): String = {
    counter.inc()
    value
  }
}