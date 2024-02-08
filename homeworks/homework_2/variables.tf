# variable "credentials" {
#   description = "My Credentials"
#   default     = "<Path to your Service Account json file>"
#   #ex: if you have a directory where this file is called keys with your service account json file
#   #saved there as my-creds.json you could use default = "./keys/my-creds.json"
# }


variable "project" {
  default     = "zoomcamp-0"
}

variable "region" {
  default     = "us-central1"
}

variable "location" {
  default     = "US"
}

variable "bq_dataset_name" {
  default     = "ny_taxi_data"
}

variable "gcs_bucket_name" {
  default     = "zoomcamp_homework2_bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}