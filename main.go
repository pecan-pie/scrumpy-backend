package main

import (
	"log"
	"net/http"
	"os"

	"github.com/gorilla/handlers"
	"github.com/gorilla/mux"
	"github.com/pecan-pie/scrumpy-backend/app"
	"github.com/pecan-pie/scrumpy-backend/model"
)

func main() {

	m, err := model.Create()

	if err != nil {
		log.Fatal("Database connection failed: %s", err.Error())
	}

	defer m.Close()

	model.CreateTestData(m)

	app := &app.App{
		Router: mux.NewRouter().StrictSlash(true),
		Model:  m,
	}

	app.SetupRouter()

	loggedRouter := handlers.LoggingHandler(os.Stdout, app.Router)
	log.Fatal(http.ListenAndServe(":5000", loggedRouter))
}
