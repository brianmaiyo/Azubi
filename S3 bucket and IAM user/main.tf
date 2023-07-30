provider "aws" {
  region = "eu-north-1" 
}

# Create an S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "brian-azubi-lab"   
  tags = {
    Name = "My Terraform S3 Bucket" 
  }
} 
#bucket ownership control 
resource "aws_s3_bucket_ownership_controls" "my_bucket" {
  bucket = aws_s3_bucket.my_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}
#The bucket ACL is set to private, read access will be granted through IAM

resource "aws_s3_bucket_acl" "my_bucket" {
  depends_on = [aws_s3_bucket_ownership_controls.my_bucket]

  bucket = aws_s3_bucket.my_bucket.id
  acl    = "private"
}

# Create an IAM user
resource "aws_iam_user" "my_user" {
  name = "Devops_Brian"  
}

# Create IAM user access keys
resource "aws_iam_access_key" "my_user_access_key" {
  user = aws_iam_user.my_user.name
}

# Create IAM policy for S3 access
resource "aws_iam_policy" "my_policy" {
  name        = "MyS3BucketPolicy"
  description = "My IAM policy for S3 bucket access"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject",
        ]
        Resource = [
          aws_s3_bucket.my_bucket.arn,
          "${aws_s3_bucket.my_bucket.arn}/*",
        ]
      },
    ]
  })
}

# Attach the policy to the IAM user
resource "aws_iam_user_policy_attachment" "my_user_attachment" {
  user       = aws_iam_user.my_user.name
  policy_arn = aws_iam_policy.my_policy.arn
}

# Outputs
output "bucket_name" {
  value = aws_s3_bucket.my_bucket.bucket
}

output "iam_user_name" {
  value = aws_iam_user.my_user.name
  sensitive = true
}

