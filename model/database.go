package model

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
)

func Create() (*gorm.DB, error) {
	db, err := gorm.Open("sqlite3", "test.db")

	db.AutoMigrate(
		&Room{},
	)

	return db, err
}

func CreateTestData(db *gorm.DB) {
	db.Create(&Room{
		Name: "1",
	})
	db.Create(&Room{
		Name: "2",
	})
}
