# variable "credentials" {
#   description = "My Credentials"
#   default     = "<Path to your Service Account json file>"
#   #ex: if you have a directory where this file is called keys with your service account json file
#   #saved there as my-creds.json you could use default = "./keys/my-creds.json"
# }


variable "project" {
  description = "Project"
  default     = "zoomcamp-0"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "US"
}

variable "bq_dataset_name" {
  description = "zoomcamp-0-bq"
  #Update the below to what you want your dataset to be called
  default     = "zoomcamp0_bq"
}

variable "gcs_bucket_name" {
  description = "zoomcamp-0-bucket"
  #Update the below to a unique bucket name
  default     = "zoomcamp0_bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}