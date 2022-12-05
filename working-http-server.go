package main

import (
  "fmt"
  "net/http"
)

func main() {
  // Define the handler for incoming HTTP requests.
  http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    // Write a simple response to the client.
    fmt.Fprintln(w, "Hello, World!")
  })

  // Start the server on port 8080.
  http.ListenAndServe(":8080", nil)
}
