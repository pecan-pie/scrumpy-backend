package app

import (
	"encoding/json"
	"net/http"
)

type Health struct {
	Status string
}

func (app *App) Health(w http.ResponseWriter, r *http.Request) {

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(&Health{
		Status: "ready",
	})
}
