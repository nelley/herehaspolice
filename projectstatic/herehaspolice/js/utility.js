

function whichBrowser(){
    // Firefox 1.0+
    var isFirefox = typeof InstallTrigger !== 'undefined';
    // At least Safari 3+: "[object HTMLElementConstructor]"
    var isSafari = Object.prototype.toString.call(window.HTMLElement).indexOf('Constructor') > 0;
    // Internet Explorer 6-11
    var isIE = /*@cc_on!@*/false || !!document.documentMode;
    // Chrome 1+
    var isChrome = !!window.chrome && !!window.chrome.webstore;
    
    if(isFirefox){
        return "F";
    }else if(isSafari){
        return "S";
    }else if(isIE){
        return "I";
    }else if(isChrome){
        return "C";
    }else{
        return "";
    }
}

function timeDiffChrome(s, e){
    var hourDiff = e - s; //in ms
                
    var minDiff = hourDiff / 60 / 1000; //in minutes
    var hDiff = hourDiff / 3600 / 1000; //in hours
    
    var humanReadable = {};
    humanReadable.hours = Math.floor(hDiff) + 8;
    humanReadable.minutes = Math.floor(minDiff - 60 * Math.floor(hDiff));
    
    return humanReadable;
}

function timeDiff(s, e){
    var hourDiff = e - s; //in ms
                
    var minDiff = hourDiff / 60 / 1000; //in minutes
    var hDiff = hourDiff / 3600 / 1000; //in hours
    
    var humanReadable = {};
    humanReadable.hours = Math.floor(hDiff);
    humanReadable.minutes = Math.floor(minDiff - 60 * humanReadable.hours);
    
    return humanReadable;
}