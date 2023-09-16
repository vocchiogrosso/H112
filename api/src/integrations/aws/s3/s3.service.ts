//

import AWS from 'aws-sdk';

// Configure AWS credentials and region
AWS.config.update({
  accessKeyId: process.env.AWS_ACCESS_KEY_ID,
  secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  region: 'your-aws-region',
});

// Create an S3 service instance
const s3 = new AWS.S3();

// Example: Upload a file to S3
const uploadParams = {
  Bucket: 'your-bucket-name',
  Key: 'your-object-key',
  Body: 'file-content',
};

s3.upload(uploadParams, (err, data) => {
  if (err) {
    console.error('Failed to upload file to S3:', err);
  } else {
    console.log('File uploaded successfully:', data.Location);
  }
});
