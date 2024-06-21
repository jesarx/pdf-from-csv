package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"

	"github.com/go-pdf/fpdf"
)

func CreatePDF(data []string, filename string) error {
	pdf := fpdf.New("P", "mm", "Letter", "")

	pdf.AddPage()
	pdf.SetFont("Times", "B", 16)

	for i, field := range data {
		pdf.Cell(40, 10, fmt.Sprintf("Field %d: %s", i+1, field))
		pdf.Ln(10)
	}

	return pdf.OutputFileAndClose(filename)
}

func main() {
	file, err := os.Open("data.csv")
	if err != nil {
		log.Fatalf("Error opening file: %v", err)
	}
	defer file.Close()

	reader := csv.NewReader(file)
	records, err := reader.ReadAll()
	if err != nil {
		log.Fatalf("Error reading CSV: %v", err)
	}

	for i, record := range records {
		filename := fmt.Sprintf("output_%d.pdf", i)
		err := CreatePDF(record, filename)
		if err != nil {
			log.Printf("Could not create pdf from row", i+1, err)
		} else {
			fmt.Print("Succes!")
		}
	}
}
