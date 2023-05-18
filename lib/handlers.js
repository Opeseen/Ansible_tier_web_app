/*
 * Request Handlers
 *
 */

// Dependencies
const helpers = require('./helpers');

const handlers = {};

handlers.index = function(callback){
    helpers.getTemplate('index',function(err,str){
      if(!err && str){
        // Add the universal header and footer
        helpers.addUniversalTemplates(str,function(err,str){
          if(!err && str){
            // Return that page as HTML
            callback(200,str);
          } else {
            callback(500,{Error:"Could not add the Universal template"});
          }
        });
      } else {
        callback(500,{Error: "Could not get templates"});
      }
    });
};

handlers.createUser = function(callback){
    helpers.getTemplate('accountCreate',function(err,str){
      if(!err && str){
        // Add the universal header and footer
        helpers.addUniversalTemplates(str,function(err,str){
          if(!err && str){
            // Return that page as HTML
            callback(200,str);
          } else {
            callback(500,{Error:"Could not add the Universal template"});
          }
        });
      } else {
        callback(500,{Error: "Could not get templates"});
      }
    });
};

handlers.loginUser = function(callback){
  helpers.getTemplate('userLogin',function(err,str){
    if(!err && str){
      // Add the universal header and footer
      helpers.addUniversalTemplates(str,function(err,str){
        if(!err && str){
          // Return that page as HTML
          callback(200,str);
        } else {
          callback(500,{Error:"Could not add the Universal template"});
        }
      });
    } else {
      callback(500,{Error: "Could not get templates"});
    }
  });
};

module.exports = handlers;