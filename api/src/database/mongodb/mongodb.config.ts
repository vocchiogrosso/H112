export const mongodbConfig = {
  uri: process.env.MONGODB_URI || 'mongodb://localhost:27017/mydatabase',
  options: {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    // Other MongoDB connection options
  },
};

//const uri = `mongodb://${databaseConfig.username}:${databaseConfig.password}@${databaseConfig.host}:${databaseConfig.port}/${databaseConfig.databaseName}`;
//const offlineUri = `mongodb://${databaseConfig.username}:${databaseConfig.password}@${databaseConfig.host}:${databaseConfig.port}/${databaseConfig.databaseName}`;