package main

import (
	"context"
	"log"
	"github.com/apache/beam/sdks/v2/go/pkg/beam"
	"github.com/apache/beam/sdks/v2/go/pkg/beam/io/textio"
	"github.com/apache/beam/sdks/v2/go/pkg/beam/io/xlang/kafkaio"
	"github.com/apache/beam/sdks/v2/go/pkg/beam/x/beamx"
)

func main() {

	// automatic
	expansionAddr := ""
	bootstrapAddr := "kafka:9092"
	topicName := "sample-topic"
	numRecords := int64(10)

	beam.Init()

	p, s := beam.NewPipelineWithRoot()
	kafkaRecords := kafkaio.Read(
		s,
		expansionAddr,
		bootstrapAddr,
		[]string{topicName},
		kafkaio.MaxNumRecords(numRecords),
		kafkaio.ConsumerConfigs(map[string]string{"auto.offset.reset": "earliest"}))

	textio.Write(s, "output.txt", kafkaRecords)
	
	if err := beamx.Run(context.Background(), p); err != nil {
		log.Fatalf("Failed to execute job: %v", err)
	}
}
