//db.getUsers( {
//   showCredentials: true,
//   showCustomData: true
//} )
////use test;
////db.auth('choto', 'pito')
//db.auth('mongoUser', 'mongoPass')

//db = db.getSiblingDB('test-database')
//
//db.createUser({
//  user: "your_user",
//  pwd: "your_password",
//  roles: [{role: "readWrite", db: "changuito"}]
//});
//show dbs
//show users
//db.createUser(
//    {
//        user: "your_user",
//        pwd: "your_password",
//        roles: [
//            {
//                role: "readWrite",
//                db: "changuito"
//            }
//        ]
//    }
//);
//db.createCollection("test");
//show dbs
//show users
//use admin;
//
//db.createUser(
//    {
//        user: "processor-api",
//        pwd: 'mongoPass',
//        roles: [
//            "userAdminAnyDatabase",
//               "dbAdminAnyDatabase",
//               "readWriteAnyDatabase"
//
//        ]
//    }
//);
////db.createUser(
////    {
////        user: 'root',
////        pwd: 'root-pass',
////        roles: [
////            { role: "clusterMonitor", db: "admin" },
////            { role: "dbOwner", db: "db_name" },
////            { role: 'readWrite', db: 'db_crashell' }
////        ]
////    }
//////)
////db.createUser(
////    {
////        user: 'wr-user',
////        pwd: 'wr-user-pass',
////        roles: [
////            {
////                role: 'readWrite',
////                db: 'changuito'
////            }
////        ]
////    }
////);
