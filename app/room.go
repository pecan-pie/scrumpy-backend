package app

import (
	"encoding/json"
	"net/http"

	"github.com/pecan-pie/scrumpy-backend/model"
)

// https://gorm.io/docs/

func (app *App) ListRoomFunction(w http.ResponseWriter, r *http.Request) {
	var rooms []model.Room
	app.Model.Find(&rooms)

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(rooms)
}
