package app

import (
	"github.com/gorilla/mux"
	"github.com/jinzhu/gorm"
)

type App struct {
	Router *mux.Router
	Model  *gorm.DB
}

func (app *App) SetupRouter() {
	app.Router.Methods("GET").Path("/room").HandlerFunc(app.ListRoomFunction)
	app.Router.Methods("GET").Path("/health").HandlerFunc(app.Health)
}
