window.vmtrcq = window.vmtrcq || [];
window.vmtrc = window.vmtrc || function () {
    window.vmtrcq.push(Array.prototype.slice.call(arguments))
};

const script = document.createElement('script');
script.src = 'https://hub.tilebox.com/main.js';
script.defer = true;
script.setAttribute('data-token', 'rQI52fw6s6frnSOR');
script.setAttribute('data-host', 'https://hub.tilebox.com');
document.head.appendChild(script);
